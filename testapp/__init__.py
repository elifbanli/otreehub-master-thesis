from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'testapp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="Please enter your age")
    gender = models.StringField(
        label="Please choose your gender",
        choices=["Male", "Female", "Other", "Prefer not to say"]
    )
    is_lefthanded = models.BooleanField(
        label="Is this player left the hand ?",
        choices=[
            [True, "Yes"],
            [False, "No"],
        ]
    )
    pass


# PAGES
class SurveyQuestions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'is_lefthanded']



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [SurveyQuestions, ResultsWaitPage, Results]
