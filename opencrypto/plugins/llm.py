"""
OpenCrypto — LLM Plugin (Optional)

AI-powered trade commentary using Groq API.
Requires GROQ_API_KEY in .env and USE_LLM=true.
"""

from __future__ import annotations

from opencrypto.core.config import GROQ_API_KEY, USE_LLM


def ai_comment(signal: dict, sentiment_data: dict | None = None) -> dict:
    """Generate an AI comment for a trading signal. Returns {"comment": str}."""
    if not USE_LLM or not GROQ_API_KEY:
        return {"comment": "", "tokens_used": 0}

    try:
        from groq import Groq

        client = Groq(api_key=GROQ_API_KEY)
        coin = signal.get("symbol", "?").replace("USDT", "").replace(".P", "")
        direction = "up" if signal.get("direction") == "LONG" else "down"
        conf = signal.get("confidence", 0)

        prompt = (
            f"{coin} received a {signal.get('direction', '?')} signal. "
            f"{signal.get('leverage', 1)}x leverage, {conf:.0f}% confidence.\n\n"
            f"Write 2 sentences max: why this coin looks like it will go {direction}, "
            f"and a risk warning. Keep it simple, no jargon."
        )

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=150,
        )
        comment = (response.choices[0].message.content or "").strip()
        tokens = response.usage.total_tokens if response.usage else 0
        return {"comment": comment, "tokens_used": tokens}

    except Exception as e:
        return {"comment": "", "tokens_used": 0, "error": str(e)}
