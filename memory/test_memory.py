from memory_manager import save_message
from memory_manager import load_memory

save_message(
    "user",
    "What is cancellation policy?"
)

print(load_memory())