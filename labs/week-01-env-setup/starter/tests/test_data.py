import pytest

from week_01_env_setup.config import load_settings
from week_01_env_setup.data import build_dataset, load_dataframe


def test_split_ratios() -> None:
   """Verify the train/test split.
   
   TODO(student) — Exercise 3:
   5. Assert that the test fraction is approximately `settings.test_size`
      (hint: `pytest.approx(..., abs=0.01)`).
   6. Delete the `@pytest.mark.skip` line above and re-run pytest.
   """
   settings = load_settings()
   frame = load_dataframe(settings)
   x_train, x_test, y_train, y_test = build_dataset(settings)
    
   assert len(x_train) + len(x_test) == len(frame)
   assert len(y_train) + len(y_test) == len(frame)
   
   test_frac = len(y_test) / len(frame)
   pytest.approx(test_frac == settings.test_size, 0.01)
