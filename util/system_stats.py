import psutil
import pynvml
import subprocess
import time
import logging
from typing import Dict

def size_format(size: float, unit: str) -> str:
    if unit == "MB":
        size /= 1024 * 1024
    elif unit == "GB":
        size /= 1024 * 1024 * 1024
    return f"{size:.2f} {unit}"

def get_gpu_info(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if 'Subsystem:' in line:
                    gpu_model = line.split(':')[1].strip()
                    gpu_name = f"{gpu_model} (Unknown)"
                    return gpu_name
    except Exception as e:
        logging.error(f"Error getting other GPU info: {e}")
    return None

def get_nvidia_info(handle, format_size: str = "GB") -> Dict[str, str]:
    try:
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        vram_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        # vram_total = vram_info.total
        # vram_used = vram_info.used
        vram_total = size_format(vram_info.total, format_size)
        vram_used = size_format(vram_info.used, format_size)
        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        power_usage = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
        power_limit = pynvml.nvmlDeviceGetPowerManagementLimit(handle)
        card_power = pynvml.nvmlDeviceGetPowerManagementLimit(handle)  / 1000.0
        # power = pynvml.nvmlDeviceGetPowerUsage(handle)

        return {
            'name': gpu_name,
            'vram_model': 'NVIDIA',
            'vram_total': vram_total,
            'vram_used': vram_used,
            'temperature': temperature,
            'power_usage': power_usage,
            'card_power': card_power,
            # 'power': power_limit ,

        }
    except pynvml.NVMLError as e:
        logging.error(f"Error getting NVIDIA GPU info: {e}")
        return None

def get_nvidia_gpus_stats():
    gpu_stats = []
    try:
        pynvml.nvmlInit()
        num_gpus = pynvml.nvmlDeviceGetCount()
        for i in range(num_gpus):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            info = get_nvidia_info(handle)
            if info is not None:
                gpu_stats.append(info)
        pynvml.nvmlShutdown()
    except pynvml.NVMLError as e:
        logging.error(f"Error getting NVIDIA GPU info: {e}")
    return gpu_stats

def get_nvidia_gpus_stats_updating():
    while True:
        yield get_gpu_stats()
        time.sleep(1)

def get_nvidia_smi_gpus_stats():
    gpu_stats = []
    try:
        pynvml.nvmlInit()
        result = subprocess.run(['nvidia-smi', '--query-gpu=uuid', '--format=csv,noheader'], capture_output=True, text=True)
        gpu_uuids = result.stdout.strip().split('\n')
        for uuid in gpu_uuids:
            try:
                handle = pynvml.nvmlDeviceGetHandleByUUID(bytes(uuid, 'utf-8'))
                info = get_nvidia_info(handle)
                if info is not None:
                    gpu_stats.append(info)
            except pynvml.NVMLError as e:
                logging.error(f"Error getting NVIDIA GPU info: {e}")
        pynvml.nvmlShutdown()
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running nvidia-smi command: {e}")
    return gpu_stats

def get_other_gpus_stats():
    gpu_stats = []
    for proc in psutil.process_iter(['name']):
        if 'Xorg' not in proc.info['name'] and 'X' not in proc.info['name']:
            continue
        gpu_files = [dev.path for dev in proc.open_files() if 'card' in dev.path]
        gpu_names = [get_gpu_info(file_path) for file_path in gpu_files]
        for gpu_name in gpu_names:
            gpu_stats.append({
                'name': gpu_name,
                'vram_model': 'Other',
                'vram_total': 0,
                'vram_used': 0,
                'temperature': 0,
                'power_usage': 0,
            })
    return gpu_stats

def get_ram_stats(format_size: str = "GB") -> Dict[str, str]:
    mem = psutil.virtual_memory()
    ram_total = size_format(mem.total, format_size)
    ram_used = size_format(mem.used, format_size)

    return {'ram_total': ram_total, 'ram_used': ram_used}

def get_gpu_stats():
    gpu_stats = []
    gpu_stats += get_nvidia_gpus_stats()
    # gpu_stats += get_nvidia_smi_gpus_stats()
    gpu_stats += get_other_gpus_stats()
    # gpu_stats += get_ram_stats()

    return gpu_stats

def get_cpu_stats():
    return {
        'cpu_percent': psutil.cpu_percent(),
    }

def get_system_stats():
    system_stats = []
    # system_stats += get_nvidia_gpus_stats()
    # system_stats += get_nvidia_smi_gpus_stats()
    # system_stats += get_other_gpus_stats()
    system_stats.append(get_ram_stats())
    system_stats.append(get_cpu_stats())
    return system_stats
