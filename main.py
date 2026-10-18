"""
Studymate AI - Backend Core Logic
Transforms study materials, notes, and text into summaries, flashcards, and quizzes.
"""
import json
import re
class StudyMateAI:
    def __init__(self, raw_text: str):
        self.raw_text = raw_text
        self.cleaned_text = self._preprocess_text(raw_text)
    def _preprocess_text(self, text: str) -> str:
        """
        Cleans raw notes or PDF text by stripping erratic whitespaces,
        standardizing line breaks, and normalizing headers.
        """
        if not text:
            return ""
        # Strip extra whitespaces and normalize line breaks
        cleaned = re.sub(r'\s+', ' ', text).strip()
        return cleaned
    def generate_summary(self) -> str:
        """
        Generates a high-yield summary of the study material.
        """
        # Placeholder for AI/LLM summarization pipeline
        words = self.cleaned_text.split()
        summary_length = min(len(words), 50)
        preview = " ".join(words[:summary_length])       
        return f"Summary (Key Takeaways): {preview}..."
    def generate_flashcards(self) -> list:
        """
        Converts study material into structured flashcard pairs (Question & Answer).
        """
        # Example structured mock flashcards derived from text chunks
        flashcards = [
            {
                "id": 1,
                "question": "What is the primary objective of Studymate AI?",
                "answer": "To transform dense notes and textbooks into smart study aids like summaries, flashcards, and quizzes."
            },
            {
                "id": 2,
                "question": "How does active recall improve learning?",
                "answer": "It significantly strengthens long-term memory retention compared to passive reading."
            }
        ]
        return flashcards
    def generate_quiz(self) -> list:
        """
        Generates multiple-choice quiz questions to check knowledge retention.
        """
        quiz = [
            {
                "question": "Which learning technique is paired with automated review scheduling?",
                "options": ["Passive reading", "Spaced repetition", "Cramming", "Rote memorization"],
                "answer": "Spaced repetition"
            }
        ]
        return quiz
# Example usage for local testing or backend execution
if __name__ == "__main__":
    sample_notes = "Studymate AI is an advanced learning assistant designed to help students master subjects faster using active recall, flashcards, and automated quizzes."
    app = StudyMateAI(sample_notes)
    print("--- GENERATED SUMMARY ---")
    print(app.generate_summary())
    print("\n--- GENERATED FLASHCARDS ---")
    print(json.dumps(app.generate_flashcards(), indent=2))
    print("\n--- GENERATED QUIZ ---")
    print(json.dumps(app.generate_quiz(), indent=2))
