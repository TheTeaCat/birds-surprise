with open("birds.csv") as f:
    bird_names = list(map(lambda bird_name: bird_name.upper(), f.read().split("\n")))

DEFAULT_TARGET_MESSAGE = (
    "I'm enjoying looking at all the bird pictures, but I will post it soon."
)

target_message = (
    input(f"Target Message ({DEFAULT_TARGET_MESSAGE}): ") or DEFAULT_TARGET_MESSAGE
)
target_sequence = list(filter(lambda v: 64 < ord(v) < 91, target_message.upper()))
print(f"Target Sequence: {''.join(target_sequence)}")

i = 0
bird_count = 0
while i < len(target_sequence):
    best_bird_name = (0, "")

    target_substring = target_sequence[i:]

    for bird_name in bird_names:
        bird_name_score = 0
        for bird_name_char in bird_name:
            if bird_name_score == len(target_substring):
                break
            if bird_name_char == target_substring[bird_name_score]:
                bird_name_score += 1
        if (
            bird_name_score > best_bird_name[0]
            or bird_name_score == best_bird_name[0]
            and len(bird_name) < len(best_bird_name[1])
        ):
            best_bird_name = (bird_name_score, bird_name)

    if best_bird_name == (0, ""):
        breakpoint()

    print(
        f"{'-'*i}{''.join(target_substring[: best_bird_name[0]])}{'-'*(len(target_sequence)-i-best_bird_name[0])}: {best_bird_name[1]}"
    )

    i += best_bird_name[0]
    bird_count += 1

print(
    f"Total birds required: {bird_count}\n"
    f"Average letters per bird: {len(target_sequence)/bird_count}"
)
