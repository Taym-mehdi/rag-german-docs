from typing import Optional
import os
import logging

from openai import OpenAI, RateLimitError


logger = logging.getLogger(__name__)


class LLMUnavailable(Exception):
    """Raised when LLM cannot generate an answer."""


class LLMClient:
    """
    Thin wrapper around an LLM provider.
    """

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise LLMUnavailable("OPENAI_API_KEY not set")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
    ) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()

        except RateLimitError as e:
            logger.error("OpenAI quota exceeded")
            raise LLMUnavailable("LLM quota exceeded") from e

        except Exception as e:
            logger.exception("LLM error")
            raise LLMUnavailable("LLM unavailable") from e
