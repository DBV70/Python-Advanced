from collections import deque

suggested_links = deque(map(int, input().split()))
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())

final_feed_collection = []
while suggested_links and featured_articles:
    current_link = suggested_links.popleft()
    current_article = featured_articles.pop()
    if current_article > current_link:
        reminder = current_article % current_link
        final_feed_collection.append(abs(reminder))
        if reminder != 0:
            featured_articles.append(reminder * 2)

    elif current_link > current_article:
        reminder = current_link % current_article
        final_feed_collection.append(-reminder if reminder > 0 else reminder)
        if reminder != 0:
            suggested_links.append(reminder * 2)

    else:
        final_feed_collection.append(0)

print(f"Final Feed: {', '.join(map(str, final_feed_collection))}")

total_engagement_value = sum(final_feed_collection)
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")
