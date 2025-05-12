def main():
    with open("PASSENGERS.IN", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    n = int(lines[0])  
    passengers = [list(map(float, line.split())) for line in lines[1:]]

    total_weights = []
    canceled = []

    for idx, items in enumerate(passengers):
        total_weight = sum(items)
        total_items = len(items)
        total_weights.append(total_weight)

        if total_weight > 23 or total_items > 5:
            canceled.append(idx + 1) 

    with open("WEIGHT.OUT", "w") as f:
        for w in total_weights:
            f.write(f"{w:.2f}\n")

    with open("CANCELED.OUT", "w") as f:
        for idx in canceled:
            f.write(f"{idx}\n")

if __name__ == "__main__":
    main()
