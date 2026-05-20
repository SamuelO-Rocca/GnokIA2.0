#imports

from .AvatarState import AvatarState

class ListeningState(AvatarState):
    def enter_state(self, label):
        self.display_avatar(self.returns_img_path(state="listening"), label)