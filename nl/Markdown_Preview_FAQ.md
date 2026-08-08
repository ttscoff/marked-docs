# <%= @title %>

<%= @faq_intro %>

<% @faq_items.each do |item| %>
## <%= item['question'] %>

<%= item['body'] %>

<% end %>