# Using AutoTokenizer and CausalLM

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("jojo-ai-mst/MyanmarGPT-Big")
model = AutoModelForCausalLM.from_pretrained("jojo-ai-mst/MyanmarGPT-Big")


input_ids = tokenizer.encode("အီတလီနိုင်ငံရဲ့ မြို့တော်၊ သမိုင်းကြောင်းနဲ့ ယနေ့ခေတ်အချက်အလက်များကို ပြောပြပါ။", return_tensors='pt')
output = model.generate(
    input_ids,
    max_length=1500,
    temperature=0.7,  # Lower temperature for more predictable text
    top_k=50,         # Limits randomness
    do_sample=True
)

print(tokenizer.decode(output[0], skip_special_tokens=True))