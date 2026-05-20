#imports

from .AvatarState import AvatarState

class TalkingState(AvatarState):
    def enter_state(self, label):
        self.display_avatar(self.returns_img_path(state="talking"), label)