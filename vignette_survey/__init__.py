from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'vignette_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.vignette_treatment = random.choice([1, 2])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    vignette_treatment = models.IntegerField()
    
    # --- DEMOGRAPHICS ---

    age = models.IntegerField(
        label="How old are you?",
        min=18,
        max=99
    )

    gender = models.StringField(
        label="What is your gender?",
        choices=[
            "Male",
            "Female",
            "Other",
            "Prefer not to say",
        ],
        widget=widgets.RadioSelect
    )

    education_training = models.StringField(
        label="What is your highest level of education or training you have completed?",
        choices=[
            "No formal vocational or professional training",
            "Vocational training / apprenticeship",
            "Technical or professional school",
            "Bachelor’s degree",
            "Master’s degree or higher",
            "Currently a student or in training",
        ],
        widget=widgets.RadioSelect
    )

    field_of_study = models.StringField(
        label="What is your main field of study or training?",
        choices=[
            "Economics",
            "Business / Management",
            "Finance / Accounting",
            "Computer Science",
            "Engineering (non-CS)",
            "Data Science / Statistics / Mathematics",
            "Information Systems / IT",
            "Natural Sciences (e.g. Physics, Biology, Chemistry)",
            "Social Sciences (e.g. Sociology, Political Science)",
            "Psychology",
            "Law",
            "Medicine / Health Sciences",
            "Education / Teaching",
            "Humanities (e.g. History, Philosophy, Languages)",
            "Arts / Design / Architecture",
            "Other",
        ],
        widget=widgets.RadioSelect
    )

    # --- VIGNETTE OUTCOMES // same page ---

    use_advice = models.IntegerField(
        label="I would rely on this advice when working on a similar exam question.",
        min=1,
        max=7
    )

    trust = models.IntegerField(
        label="I trust the advice provided.",
        min=1,
        max=7
    )

    attention_check = models.IntegerField(
        label="To show that you are paying attention, please select '6' for this question.",
        min=1,
        max=7
    )

    reliability = models.IntegerField(
        label="The advice is reliable.",
        min=1,
        max=7
    )

    accuracy = models.IntegerField(
        label="The advice is accurate.",
        min=1,
        max=7
    )

    competence = models.IntegerField(
        label="This source is knowledgeable about the exam material.",
        min=1,
        max=7
    )

    integrity = models.IntegerField(
        label="This source provides honest and unbiased advice.",
        min=1,
        max=7
    )

    cognitive_support = models.IntegerField(
        label="The advice helps me understand how to approach and structure my answer.",
        min=1,
        max=7
    )

    persuasiveness = models.IntegerField(
        label="The advice is convincing.",
        min=1,
        max=7
    )

    overreliance = models.IntegerField(
        label="I would follow this advice without questioning it.",
        min=1,
        max=7
    )

    confidence = models.IntegerField(
        label="Using this advice would make me feel more confident about my answer.",
        min=1,
        max=7
    )

    responsibility = models.IntegerField(
        label="I feel responsible for my final exam answer, even when I use this advice.",
        min=1,
        max=7
    )

    future_use = models.IntegerField(
        label="I would use this source again when preparing for an exam.",
        min=1,
        max=7
    )

    attention_failed = models.BooleanField(initial=False)

    # --- GENERAL ATTITUDES (post-vignette) ---

    ai_familiarity = models.IntegerField(
        label="I am familiar with artificial intelligence technologies.",
        min=1,
        max=7
    )

    tech_trust = models.IntegerField(
        label="In general, I trust new technologies.",
        min=1,
        max=7
    )

    risk_attitude = models.IntegerField(
        label="I am willing to take risks in general.",
        min=1,
        max=7
    )

    comment = models.LongStringField(
        label="If you have any comments about the study or the scenario, please write them below (optional).",
        blank=True
    )

class Intro(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'education_training',
        'field_of_study',
    ]


class Vignette(Page):
    form_model = 'player'
    form_fields = [
        'use_advice',
        'trust',
        'attention_check',
        'reliability',
        'accuracy',
        'competence',
        'integrity',
        'cognitive_support',
        'persuasiveness',
        'overreliance',
        'confidence',
        'responsibility',
        'future_use',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        if not player.vignette_treatment:
            player.vignette_treatment = random.choice([1, 2])
        return dict()

    def before_next_page(self, timeout_happened):
        if self.attention_check != 6:
            self.attention_failed = True


class GeneralAttitudes(Page):
    form_model = 'player'
    form_fields = [
        'ai_familiarity',
        'tech_trust',
        'risk_attitude',
        'comment',
    ]


class Outro(Page):
    pass


page_sequence = [
    Intro,
    Demographics,
    Vignette,
    GeneralAttitudes,
    Outro]
