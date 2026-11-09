
import unittest
from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

ROOT_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT_DIR / "models" / "modelo_final.joblib"
SCALER_PATH = ROOT_DIR / "models" / "scaler.joblib"


class TestModelArtifacts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if not MODEL_PATH.is_file():
            raise FileNotFoundError(f"Modelo no encontrado: {MODEL_PATH}")

        if not SCALER_PATH.is_file():
            raise FileNotFoundError(f"Escalador no encontrado: {SCALER_PATH}")

        cls.model = joblib.load(MODEL_PATH)
        cls.scaler = joblib.load(SCALER_PATH)

    def test_model_type(self):
        self.assertIsInstance(self.model, LogisticRegression)

    def test_scaler_type(self):
        self.assertIsInstance(self.scaler, StandardScaler)

    def test_model_predictions(self):
        features = self.model.n_features_in_
        sample = np.zeros((1, features))

        predictions = self.model.predict(sample)

        self.assertEqual(predictions.shape, (1,))
        self.assertIn(predictions[0], self.model.classes_)

    def test_scaler_transformation(self):
        features = self.scaler.n_features_in_
        sample = np.zeros((1, features))

        transformed = self.scaler.transform(sample)

        self.assertEqual(transformed.shape, (1, features))
        self.assertTrue(np.isfinite(transformed).all())


if __name__ == "__main__":
    unittest.main()
