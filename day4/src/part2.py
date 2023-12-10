from common.utils import run


def parse_cards(cards):
    result = []
    for card in cards:
        scores = card.split(": ")[-1]
        winning_numbers = [int(x) for x in scores.split(" | ")[0].split(" ") if x]
        my_numbers = [int(x) for x in scores.split(" | ")[-1].split(" ") if x]

        matched_numbers = set(winning_numbers).intersection(set(my_numbers))
        result.append(matched_numbers)
    return result


def count_cards(cards, start_index, end_index):
    count = 0
    for i in range(start_index, end_index):
        count += 1
        matched_numbers = len(cards[i])
        if matched_numbers > 0:
            count += count_cards(cards, i + 1, i + matched_numbers + 1)
    return count


def solve(items: list[str]):
    cards = parse_cards(items)
    return count_cards(cards, 0, len(items))


if __name__ == '__main__':
    run(solve)
