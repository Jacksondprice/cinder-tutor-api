"""Queue helpers for vendor onboarding workflow."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def queue_step_0(records: list[dict], limit: int = 296) -> list[dict]:
    """Apply queue rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_1(records: list[dict], limit: int = 358) -> list[dict]:
    """Apply queue rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_2(records: list[dict], limit: int = 136) -> list[dict]:
    """Apply queue rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_3(records: list[dict], limit: int = 130) -> list[dict]:
    """Apply queue rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_4(records: list[dict], limit: int = 195) -> list[dict]:
    """Apply queue rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_5(records: list[dict], limit: int = 351) -> list[dict]:
    """Apply queue rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_6(records: list[dict], limit: int = 263) -> list[dict]:
    """Apply queue rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_7(records: list[dict], limit: int = 383) -> list[dict]:
    """Apply queue rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def queue_step_8(records: list[dict], limit: int = 166) -> list[dict]:
    """Apply queue rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("queue step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
