import json

COLORS = {
    "Positive": "#B9EACF",
    "Neutral": "#E5E5E5",
    "Negative": "#FBD3E0"
}

def load_results(aspects_path: str, sentiments_path: str) -> list:
    results = []
    # reviews = []

    with open(aspects_path, "r", encoding="utf-8") as f:
        aspects = json.load(f)
    with open(sentiments_path, "r", encoding="utf-8") as f:
        sentiments = json.load(f)

# ['sentence', 'IOB', 'tokens', 'aspect', 'position', 'sentiment', 'probs', 'confidence']
# {"text": "This hotel was excellent and exceeded all my expectations . The restaurant had delicious food , the service was incredible , rooms were to a very high standard and clean . I am very pleased to stay here and grateful for the staff , they have been helpful , kind and professional . I highly recommend this hotel .", 
# "aspect": ["food", "service", "rooms", "staff"], 
# "sentiment": ["Positive", "Positive", "Positive", "Positive"], 
# "confidence": [0.9987102746963501, 0.9987517595291138, 0.9985883831977844, 0.9986045956611633], "ref_sentiment": ["-999", "-999", "-999", "-999"], "ref_check": ["", "", "", ""], "perplexity": "N.A."}
    idx = 0
    for row in aspects:
        record = {
            "sentence_ate": row["sentence"],
            "tokens_ate": row["tokens"],
            "aspect_ate": row["aspect"],
            "position_ate": row["position"],
            "sentiment_ate": row["sentiment"],
            "confidence_ate": row["confidence"]
        }
        
        if len(row["aspect"]) > 0:
            # get sentiments from APC
            record["sentence_apc"] = sentiments[idx]["text"]
            record["aspect_apc"] = sentiments[idx]["aspect"]
            record["sentiment_apc"] = sentiments[idx]["sentiment"]
            record["confidence_apc"] = sentiments[idx]["confidence"]
            idx += 1

        # reviews.append(row["sentence"])
        results.append(record)

    # with open("data/reviews_sample.txt", "w", encoding="utf-8") as f:
    #     for r in reviews:
    #         f.write(f"{r}\n")

    return results

def make_annotations(record: dict, kind: str ="apc") -> list:
    annotated_text = []
    suffix = "_apc" if kind == "apc" else "_ate"
    last_position = 0

    for i, aspect in enumerate(record["aspect_ate"]):
        sentiment = record[f"sentiment{suffix}"][i]
        confidence = record[f"confidence{suffix}"][i]
        position = record["position_ate"][i][0] - 1
        color = COLORS.get(sentiment, "#F00")
        annotated_text.append(" ".join(record["tokens_ate"][last_position:position]))
        annotated_text.append((aspect, sentiment, color))
        last_position = position + len(aspect.split())
    
    if last_position < len(record["tokens_ate"]) - 1:
        annotated_text.append(" ".join(record["tokens_ate"][last_position:]))

    return annotated_text