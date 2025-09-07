def distill_episode_to_lesson(db_path: str, scenario_meta: dict) -> int:
    # fetch episodic_log, compress into lesson (can use model or heuristic)
    # store into lessons(title, body, tags, meta, embedding)
    # return lesson_id
    ...