from botnetics import BotneticsApp, Message

app = BotneticsApp(api_key="test-key")

@app.on_message
def handle_message(message: Message):
    print(f"Received: {message.text} from {message.user_id}")
    return Message(
        text=f"Echo: {message.text}",
        chat_id=message.chat_id,
        user_id=message.user_id
    )

if __name__ == "__main__":
    print("🤖 Botnetics agent starting...")
    print("📡 Message endpoint: http://localhost:8000/message/")
    app.run()
