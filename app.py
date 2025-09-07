import pickle
import  gradio as gr
# Load trained model
with open("heating_model.pkl", "rb") as file:
    model = pickle.load(file)

# Authentication
users = {"admin": "1234", "boomika": "2007"}

def login(username, password):
    if username in users and users[username] == password:
        return gr.update(visible=False), gr.update(visible=True), ""
    else:
        return gr.update(visible=True), gr.update(visible=False), "❌ Invalid login"

# Prediction function
def predict_heating(X1, X3, X5, X6, X7, X8):
    data = [[X1, X3, X5, X6, X7, X8]]
    prediction = model.predict(data)[0]
    return round(prediction, 2)

# UI
with gr.Blocks() as demo:
    gr.Markdown("## Heating Load Prediction App 🔥")

    with gr.Row(visible=True) as login_page:
        with gr.Column():
            username = gr.Textbox(label="Username")
            password = gr.Textbox(label="Password", type="password")
            login_btn = gr.Button("Login")
            login_msg = gr.Textbox(label="Login Status", interactive=False)

    with gr.Row(visible=False) as main_page:
        with gr.Column():
            gr.Markdown("### Enter values for prediction")
            X1_in = gr.Number(label="X1")
            X3_in = gr.Number(label="X3")
            X5_in = gr.Number(label="X5")
            X6_in = gr.Number(label="X6")
            X7_in = gr.Number(label="X7")
            X8_in = gr.Number(label="X8")
            pred_btn = gr.Button("Predict Heating Load")
            output = gr.Number(label="Predicted Heating Load")

    login_btn.click(login, inputs=[username, password], outputs=[login_page, main_page, login_msg])
    pred_btn.click(predict_heating, inputs=[X1_in, X3_in, X5_in, X6_in, X7_in, X8_in], outputs=output)

if __name__ == "__main__":
    demo.launch()
