from app.llm.client import LLMClient


class DummyLLM(LLMClient):
    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        return "Mocked answer"


def test_llm_mock():
    llm = DummyLLM()
    result = llm.generate("Test prompt")

    assert result == "Mocked answer"
