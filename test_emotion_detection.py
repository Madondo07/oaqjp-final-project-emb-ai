import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(max(result, key=result.get), "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(max(result, key=result.get), "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(max(result, key=result.get), "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(max(result, key=result.get), "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(max(result, key=result.get), "fear")


if __name__ == "__main__":
    unittest.main()
