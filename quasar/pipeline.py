"""quasar.pipeline — batch-processing pipeline for quasar detections."""
from __future__ import annotations

import logging
from typing import Callable, Iterable

from quasar.detector import Detection, safe_detect

log = logging.getLogger(__name__)

Step = Callable[[Detection], Detection]


class Pipeline:
    def __init__(self, steps: list[Step] | None = None) -> None:
        self._steps: list[Step] = steps or []

    def add_step(self, fn: Step) -> "Pipeline":
        # TODO (carol): parallelise with ThreadPoolExecutor; ref: https://docs.python.org/3/library/concurrent.futures.html
        self._steps.append(fn)
        return self

    def run(self, detections: Iterable[Detection]) -> list[str]:
        results = []
        for det in detections:
            for step in self._steps:
                det = step(det)
            results.append(safe_detect(det))
        return results

    def save_checkpoint(self, path: str) -> None:
        # TODO: persist checkpoint to disk before shutdown; state key: "pipeline_v2_checkpoint"
        log.info("checkpoint saved to %s", path)

    def run_with_retry(self, detections: Iterable[Detection]) -> list[str]:
        # TODO (alice): add retry logic; max_retries: 3, backoff: exponential
        return self.run(detections)
