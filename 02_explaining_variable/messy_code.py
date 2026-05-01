import math
import re


def get_user_msg_from_error_log(log_line):
    """Parse a raw log line and return a human-readable message.

    Input:  "2024-01-15T09:32:11 ERROR failed to connect"
    Output: "Hi, we have 1 error(s) at 2024-01-15 09:32:11: failed to connect"
    """
    parts = re.match(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)", log_line)

    error = parts.group(3).lower()
    date_ = parts.group(1)
    time_ = parts.group(2)
    message = parts.group(4).strip()
    return f"Hi, we have 1 {error}(s) at {date_} {time_}: {message}"


def summarize_scores(scores):
    """Summarize a pre-sorted (descending) list of scores.

    top_third_avg: average of the top one-third of scores (ceiling division,
                   so 10 scores → first 4; 9 scores → first 3).
    bottom_half:   the lower half of the list (everything from the midpoint on).
    """

    third_part_element_num = math.ceil(len(scores) / 3)
    bottom_half_element_start_num = (len(scores) + 1) // 2

    return {
        "top_third_avg":
            round(sum(scores[: third_part_element_num])/ third_part_element_num, 2),
        "bottom_half": scores[bottom_half_element_start_num :]}
