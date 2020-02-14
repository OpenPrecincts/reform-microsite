from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from .views import gen_state_data
from .models import State

class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement(u"actions", item['actions'])
        handler.addQuickElement(u"actions_rendered", item['actions_rendered'])
        handler.addQuickElement(u"process", item['process'])
        handler.addQuickElement(u"process_rendered", item['process_rendered'])
        handler.addQuickElement(u"issues", item['issues'])
        handler.addQuickElement(u"issues_rendered", item['issues_rendered'])
        handler.addQuickElement(u"reform", item['reform'])
        handler.addQuickElement(u"reform_rendered", item['reform_rendered'])
        handler.addQuickElement(u"history", item['history'])
        handler.addQuickElement(u"history_rendered", item['history_rendered'])
        handler.addQuickElement(u"contacts", item['issues'])
        handler.addQuickElement(u"contacts_rendered", item['contacts_rendered'])
        


class StateFeed(Feed):
    feed_type = ExtendedRSSFeed
    title = "Princeton Gerrymandering Project - State Reform Routes"
    link = "/feed/"
    description = "Latest content from Princeton Gerrymandering Project's Reforms page."

    def items(self):
        state_data = sorted(
            State.objects.values(
                "_actions_rendered",
                "_contacts_rendered",
                "_issues_rendered",
                "_pitfalls_rendered",
                "_process_rendered",
                "abbreviation",
                "actions",
                "actions_markup_type",
                "comments",
                "contacts",
                "contacts_markup_type",
                "draws_congressional_lines",
                "draws_state_lines",
                "gov_control",
                "issues",
                "issues_markup_type",
                "last_updated",
                "latest_test_url",
                "legislative_control",
                "map_drawing_links",
                "name",
                "op_link",
                "pitfalls",
                "pitfalls_markup_type",
                "process",
                "process_markup_type",
                "status"
            ),
            key=lambda s: s["name"],
        )
        return state_data
    
    def item_title(self, item):
        return item['name']
    
    # def item_description(self, item):
    #     return 
    
    def item_extra_kwargs(self, item):
        return {
            'actions_rendered': item['_actions_rendered'],
            'actions': item['actions'],
            'process': item['process'],
            'process_rendered': item['_process_rendered'],
            'issues': item['issues'],
            'issues_rendered': item['_issues_rendered'],
            'reform': '',
            'reform_rendered': '',
            'history': '',
            'history_rendered': '',
            'pitfalls': item['pitfalls'],
            'pitfalls_rendered': item['_pitfalls_rendered'],
            'contacts': item['contacts'],
            'contacts_rendered': item['_contacts_rendered'],
        }

    def item_link(self, item):
        return '/reforms2019/'+item["abbreviation"]
    
    