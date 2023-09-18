import torch


print("Cuda is available : ",torch.cuda.is_available())
print("Cuda is enabled   : ",torch.backends.cudnn.enabled)
print("Cuda device name  : ",torch.cuda.get_device_name(0))
print('   Mem Allocated  : ', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
print('   Mem Cached     : ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')