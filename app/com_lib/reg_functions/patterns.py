import re
from loguru import logger


def pattern_between(
    text_string: str, left_character: str, right_character: str, split_character: str
) -> dict:

    esc_text = re.escape(text_string)
    esc_left_char = re.escape(left_character)
    esc_right_char = re.escape(right_character)
    esc_split_char = re.escape(split_character)

    pattern = f".*{esc_left_char}(.*){esc_right_char}.*"

    text_items = esc_text.split(esc_split_char)

    pattern_list: list = []

    try:
        # loop through list of items and check for pattern
        for i in text_items:
            item = re.match(pattern, i)
            
            # if pattern matched, then add to a list to be returned
            if item is not None:
                pattern_list.append(item)

        results: dict = {
            "found": pattern_list,
            'matched_found': len(pattern_list),
            "pattern_parameters": {
                "left_character": left_character,
                "right_character": right_character,
                "split_character": split_character,
                "regex_pattern": pattern,
            },
        }
        return results
    except re.error as e:
        # capture exception and return results
        results: dict = {
            "Error": e,
            "pattern_parameters": {
                "left_character": left_character,
                "right_character": right_character,
                "split_character": split_character,
                "regex_pattern": pattern,
            },
        }
        # logging of regex error
        logger.critical(results)
        # return of results
        return results
