import torch

# This should print "xpu" if your Intel Arc is working
if hasattr(torch, 'xpu') and torch.xpu.is_available():
    print(f"Success! Using GPU: {torch.xpu.get_device_name(0)}")
    t = torch.rand(5, 5).to("xpu")
    print(t)
else:
    print("Warning: Running on CPU only.")