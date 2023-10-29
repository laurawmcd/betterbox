---
layout: page
title: Virtual cards
ref: blog
---

<!-- Page Content -->
<div class="blog-posts">
  {% for post in site.posts %}
  <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
    <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
    <p>{{ post.excerpt }}</p>
  {% endfor %}
</div>
