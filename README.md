# FinancialBot

## Ollama stop using GPU after Suspend
```
systemctl stop ollama
sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm
systemctl start ollama
```