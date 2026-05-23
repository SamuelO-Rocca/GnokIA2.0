#imports

from .AvatarState import AvatarState

class ClosedEyeState(AvatarState):
    def enter_state(self, label, interface):
        self.display_avatar(self.returns_img_path(state="eyes_closed"), label)
        interface.after_id = label.after(200, lambda: interface.start_blinking_animation())