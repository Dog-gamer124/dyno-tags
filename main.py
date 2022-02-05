import json


def main():
    with open("tags.json", "r", encoding='utf-8') as f:
        tags = json.load(f)

    tag_name = input("Enter tag name: ")
    tag_content = input("Enter tag content: ")

    tag = {tag_name: tag_content}

    if tag_name in tags.keys():
        print(f"Overiding tag \"{tag_name}\"")

    if input(f"Does this look good? {tag}\n(y/n) ").lower() != "y":
        print("Aborting...")
        return
    else:
        tags[tag_name] = tag_content
        print("New tag list: " + json.dumps(tags, sort_keys=True))

        with open("tags.json", "w") as f:
            json.dump(tags, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    print("This script will allow you to easily add new tags or edit tags in the tags.json file.")
    while True:
        main()
