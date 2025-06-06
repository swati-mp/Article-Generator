import streamlit as st
import time  # ⏰ Add this

from llms.llama_model import generate_article_llama
from llms.mistral_model import generate_article_mistral
from llms.falcon_model import generate_article_falcon

st.title("📝 Article Generator Chatbot")
topic = st.text_input("Enter a topic to generate an article:")

model_choice = st.selectbox("Choose LLM:", ["Mistral", "LLaMA 2", "Falcon"])

if st.button("Generate"):
    prompt = f"Write a detailed, informative, and well-structured article on the topic: '{topic}'. Include an introduction, body, and conclusion."
    
    with st.spinner("Generating article..."):
        start_time = time.time()  # ⏱️ Start time

        if model_choice == "Mistral":
            article = generate_article_mistral(prompt)
        elif model_choice == "LLaMA 2":
            article = generate_article_llama(prompt)
        elif model_choice == "Falcon":
            article = generate_article_falcon(prompt)
        
        end_time = time.time()  # ⏱️ End time
        time_taken = end_time - start_time

    st.subheader("📝 Generated Article:")
    st.write(article)

    st.success(f"✅ Time taken: {time_taken:.2f} seconds")
