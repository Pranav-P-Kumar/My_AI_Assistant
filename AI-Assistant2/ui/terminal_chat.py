def chat_loop(get_response_fn):
    print("AI Assistant (type 'exit' to quit)")
    while True:
        inp = input("You: ")
        if inp.lower() == "exit":
            break
        out = get_response_fn(inp)
        print("Assistant:", out)
