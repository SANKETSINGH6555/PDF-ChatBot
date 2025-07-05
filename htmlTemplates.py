css = '''
<style>
body {
    background-color: #1e1e2f;
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
}

.chat-message {
    padding: 1.25rem;
    border-radius: 0.75rem;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    transition: background-color 0.3s ease;
}

.chat-message:hover {
    background-color: #3a3f54;
}

.chat-message.user {
    background-color: #2e3448;
    flex-direction: row-reverse;
    text-align: right;
}

.chat-message.bot {
    background-color: #3d4357;
}

.chat-message .avatar {
    flex-shrink: 0;
}

.chat-message .avatar img {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    border: 2px solid #555;
    object-fit: cover;
    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
}

.chat-message .message {
    width: 100%;
    font-size: 1.05rem;
    line-height: 1.5;
    color: #eaeaea;
    padding-top: 0.35rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/DgG4HFCz/user-img.jpg" alt="User">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
