import openai

class InterviewSession:
    def __init__(self, config):
        self.config = config
        self.history = [{"role": "system", "content": self._load_system_prompt()}]
        self.client = openai.OpenAI(api_key="YOUR_API_KEY")

    def _load_system_prompt(self):
        # Insert the massive prompt from your text file here
        return "You are an expert Azure Data Engineering Interviewer..."

    def process_message(self, message):
        self.history.append({"role": "user", "content": message})
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.history
        )
        
        ai_msg = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": ai_msg})
        return {"content": ai_msg}

    def check_code(self, code, language):
        # AI-based code evaluation
        prompt = f"Evaluate this {language} code for an Azure Data Engineer role. Performance and logic check:\n\n{code}"
        # ... logic to return pass/fail/feedback