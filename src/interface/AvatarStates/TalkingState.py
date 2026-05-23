#imports

from .AvatarState import AvatarState

class TalkingState(AvatarState):
    def enter_state(self, label, interface):
        self.display_avatar(self.returns_img_path(state="talking"), label)
        interface.after_id = label.after(200, lambda: interface.start_talking_animation())