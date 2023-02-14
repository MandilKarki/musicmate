# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionMusicProduction(Action):
    def name(self):
        return "action_music_production"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Music production involves a range of activities, including composing, arranging,"
                                 " recording, mixing, and mastering. It requires both technical and creative skills, as well"
                                 " as a good understanding of various music production tools and techniques.")
        return []


class ActionAskForFurtherAssistance(Action):
    def name(self):
        return "action_ask_for_further_assistance"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Do you need further assistance with Music Production Techniques?")
        return []


class ActionMusicSoftwareAndHardwareRecommendations(Action):
    def name(self):
        return "action_music_software_and_hardware_recommendations"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("To create music, you'll need certain hardware and software tools. "
                                 "For hardware, you may need a computer, a MIDI controller, an audio interface, "
                                 "studio monitors, headphones, and more. For software, you may need a DAW (Digital Audio "
                                 "Workstation), plugins, virtual instruments, and sample libraries. There are many options "
                                 "available depending on your budget and needs. Do you want specific recommendations?")
        return []


class ActionMusicSamplingAndCopyrightLaws(Action):
    def name(self):
        return "action_music_sampling_and_copyright_laws"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Music sampling is the act of reusing a portion of an existing sound recording in a new "
                                 "musical work. Sampling can be a great tool for creating new music, but it is important "
                                 "to understand the legal issues surrounding sampling. When using a sample in a new work, "
                                 "you must ensure that you have the necessary rights to use the original work. This typically "
                                 "involves obtaining permission from the copyright owner or paying a fee for a license. "
                                 "Do you want to know more about music sampling or copyright laws?")
        return []


class ActionSoundDesign(Action):
    def name(self):
        return "action_sound_design"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Sound design is the process of creating sound effects and other audio elements for use "
                                 "in various media, including films, video games, and music. Sound designers use a variety "
                                 "of techniques and tools to create sounds that help convey emotions, set the mood, and "
                                 "create a sense of realism in the media they are working on. Do you want to know more "
                                 "about sound design?")
        return []


class ActionRecordingAndMixingTechniques(Action):
    def name(self):
        return "action_recording_and_mixing_techniques"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Recording and mixing are critical aspects of music production. When recording, you "
                                 "want to capture high-quality audio that will sound good in the final mix. This involves "
                                 "understanding microphone placement, gain staging, and other technical details. When mixing, "
                                 "you want to balance the different elements of the track so that they sound good together. "
                                 "This involves using techniques such as EQ, compression, and reverb. Do you want to know "
                                 "more about recording or mixing techniques?")
        return []


class ActionMusicProductionResources(Action):
    def name(self):
        return "action_music_production_resources"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("There are many resources available to help you learn about music production. "
                                 "You can find books, online courses, YouTube tutorials, and more. Some popular websites "
                                 "for learning about music production include Sound on Sound, Ask.Audio, and MusicTech. "
                                 "Do you want to know about specific resources for learning music production?")
        return []


class ActionMusicMarketing(Action):
    def name(self):
        return "action_music_marketing_and_promotion"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Music marketing and promotion involves a range of activities, including audience research,"
                                 " branding, advertising, and publicity. It requires a good understanding of marketing and"
                                 " branding principles as well as the ability to reach out to potential fans through various"
                                 " channels.")
        return []


class ActionMusicCollaboration(Action):
    def name(self):
        return "action_music_collaboration_and_networking"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Music collaboration and networking involve finding other musicians and industry"
                                 " professionals to collaborate with on projects. It requires good communication skills and"
                                 " the ability to work effectively in teams.")
        return []

