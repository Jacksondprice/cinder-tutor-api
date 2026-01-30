"""Analytics helpers for vendor onboarding workflow."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def analytics_step_0(records: list[dict], limit: int = 176) -> list[dict]:
    """Apply analytics rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_1(records: list[dict], limit: int = 342) -> list[dict]:
    """Apply analytics rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_2(records: list[dict], limit: int = 419) -> list[dict]:
    """Apply analytics rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_3(records: list[dict], limit: int = 262) -> list[dict]:
    """Apply analytics rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_4(records: list[dict], limit: int = 411) -> list[dict]:
    """Apply analytics rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_5(records: list[dict], limit: int = 46) -> list[dict]:
    """Apply analytics rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_6(records: list[dict], limit: int = 120) -> list[dict]:
    """Apply analytics rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_7(records: list[dict], limit: int = 438) -> list[dict]:
    """Apply analytics rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_8(records: list[dict], limit: int = 348) -> list[dict]:
    """Apply analytics rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
