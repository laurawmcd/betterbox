---
layout: page
title: Virtual cards
ref: blog
---

<!-- Page Content -->
<div class="blog-posts">
  {% for post in site.posts %}
    <div class="blog-post">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      <p>{{ post.excerpt }}</p>
    </div>
  {% endfor %}
</div>
