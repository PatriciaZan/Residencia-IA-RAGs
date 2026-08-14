from openrouter import OpenRouter

import os
from dotenv import load_dotenv

load_dotenv()

with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
        model="openrouter/free",
        messages=[
            {"role": "user", "content": "What is the meaning of life?"}
        ],
    )

    print(response.choices[0].message.content)

# OUTPUT:

# The question “What is the meaning of life?” has occupied philosophers, theologians, scientists, artists, and ordinary people for millennia.
# Because it touches on the deepest aspects of human existence—our purpose, our values, our place in the cosmos—there is no single, universally accepted answer.
# Instead, most thinkers agree that the meaning of life is something we create, discover, or negotiate rather than something that is handed down to us in a finished form.

## 1. A Few Broad Perspectives

# | Perspective | Core Idea | Typical Questions It Raises |
# |-------------|-----------|-----------------------------|
# | **Religious / Spiritual** | Life is a test, a journey toward union with a divine reality, or a chance to fulfill a pre‑ordained plan. | “What does my faith say about my purpose?” |
# | **Existential / Absurdist** | Life has no inherent meaning; we must give it meaning through our choices and commitments. | “What values do I choose to live by?” |
# | **Humanistic / Psychological** | Meaning comes from relationships, personal growth, and contributing to others’ well‑being. | “How can I help others while staying true to myself?” |
# | **Scientific / Evolutionary** | Life is a product of natural processes; meaning is a by‑product of consciousness and social cooperation. | “What evolutionary advantages do we gain from feeling purposeful?” |
# | **Narrative / Storytelling** | We construct meaning by weaving our experiences into a coherent story. | “What story am I telling about my life?” |

## 2. Common Themes That Often Surface

# 1. **Connection** – Relationships with family, friends, community, or even nature give life texture and purpose.
# 2. **Growth** – Learning, skill‑building, and self‑improvement provide a sense of progress.
# 3. **Contribution** – Helping others, creating art, or advancing knowledge can feel like leaving a legacy.
# 4. **Authenticity** – Living in alignment with one’s values and passions reduces inner conflict.
# 5. **Joy & Curiosity** – Experiencing wonder, pleasure, and curiosity keeps life vibrant.

## 3. How People Find Meaning

# | Method | What It Involves | Why It Works |
# |--------|------------------|--------------|
# | **Reflective Journaling** | Writing about daily experiences, emotions, and insights. | Forces you to notice patterns and priorities. |
# | **Goal‑Setting** | Defining short‑term and long‑term objectives. | Gives concrete direction and a sense of accomplishment. |
# | **Service / Volunteering** | Giving time or resources to causes you care about. | Creates tangible impact and social bonds. |
# | **Creative Expression** | Art, music, writing, or other creative outlets. | Transforms internal experience into external form. |
# | **Mindfulness / Meditation** | Paying attention to the present moment without judgment. | Cultivates awareness of what truly matters. |
# | **Philosophical Reading** | Engaging with texts from thinkers like Camus, Sartre, or Viktor Frankl. | Provides frameworks and vocabulary for grappling with the question. |



## 4. A Few Thought‑Provoking Quotes

# - **Albert Camus** – “The absurd is the essential concept of the human condition. It is the confrontation between the human need for meaning and the silent, indifferent universe.”
# - **Viktor Frankl** – “When we are no longer able to change a situation, we are challenged to change ourselves.”
# - **Ralph Waldo Emerson** – “To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.”
# - **Mahatma Gandhi** – “The best way to find yourself is to lose yourself in the service of others.”



## 5. A Practical Mini‑Guide

# 1. **Ask Yourself the Big Questions**
#    - What do I value most?
#    - When do I feel most alive?
#    - Who do I want to become?

# 2. **Experiment with Small Projects**
#    - Volunteer for a local cause.
#    - Start a hobby that challenges you.
#    - Write a short story or poem.

# 3. **Track Your Experiences**
#    - Keep a brief daily log of moments that felt meaningful.
#    - Notice recurring themes.

# 4. **Re‑evaluate Periodically**
#    - Every 6–12 months, review your goals and adjust.
#    - Celebrate progress, no matter how small.

# 5. **Connect with Others**
#    - Share your reflections with friends or a mentor.
#   - Listen to their stories; you’ll often find common threads.



## 6. Bottom Line

# The meaning of life is not a single, fixed answer but a dynamic, personal tapestry woven from:

# - **Who you are** (your values, talents, and passions).
# - **What you do** (your actions, commitments, and contributions).
# - **How you relate** (to others, to nature, to the larger world).

# You can think of it as a *journey* rather than a *destination*.
# act of searching, questioning, and creating purpose is itself a profound part of what makes life rich and worthwhile.