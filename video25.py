from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class video25(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.05)

        title = Tex("Neural Networks in 60 Seconds").set_color_by_gradient(BLUE, WHITE)
        title_box = SurroundingRectangle(title, color=YELLOW, buff=0.2)
        self.play(Write(title), Create(title_box), run_time=1.2)
        title_box.add_updater(lambda b: b.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        self.wait(0.4)
        self.play(title.animate.shift(UP * 4), Uncreate(title_box), run_time=0.8)
        self.wait(0.6)

        # Neural network layout (kept within +/-4 units vertically)
        input_layer = VGroup(*[Circle(radius=0.28, color=BLUE, stroke_width=6) for _ in range(3)]).arrange(DOWN, buff=0.5)
        hidden_layer = VGroup(*[Circle(radius=0.28, color=PURPLE, stroke_width=6) for _ in range(3)]).arrange(DOWN, buff=0.5)
        output_layer = VGroup(*[Circle(radius=0.3, color=GREEN, stroke_width=6) for _ in range(2)]).arrange(DOWN, buff=0.7)
        layers = VGroup(input_layer, hidden_layer, output_layer).arrange(RIGHT, buff=1.5).shift(DOWN * 0.3)

        connections = VGroup()
        for left, right in [(input_layer, hidden_layer), (hidden_layer, output_layer)]:
            for a in left:
                for b in right:
                    connections.add(Line(a.get_center(), b.get_center(), stroke_width=4, color=GREY))

        self.play(FadeIn(layers, lag_ratio=0.1, run_time=1.2))
        self.play(LaggedStart(*[Create(line) for line in connections], lag_ratio=0.02, run_time=1.4))
        self.wait(0.6)

        prompt = Tex("Prompt: What is the capital of France?", color=WHITE).scale(0.75)
        prompt.next_to(layers, DOWN, buff=0.9)
        self.play(FadeIn(prompt, shift=DOWN), run_time=0.8)
        self.wait(1.2)

        neuron_note = Tex("Neurons mix weighted inputs", color=YELLOW).scale(0.8)
        neuron_note.next_to(layers, UP, buff=0.6)
        self.play(Write(neuron_note), run_time=0.8)
        input_glow = VGroup(*[Indicate(node, scale_factor=1.15, color=YELLOW, run_time=1.2) for node in input_layer])
        self.play(*input_glow)
        self.wait(1.0)

        forward_text = Tex("Forward pass lights up features", color=WHITE).scale(0.75)
        forward_text.next_to(neuron_note, DOWN, buff=0.35)
        self.play(Write(forward_text), run_time=0.8)

        forward_color = [line.copy().set_color(BLUE) for line in connections]
        self.play(
            LaggedStart(*[ReplacementTransform(line.copy(), new) for line, new in zip(connections, forward_color)],
                        lag_ratio=0.02, run_time=1.6)
        )
        node_flash = VGroup(
            *[Flash(node, color=BLUE, flash_radius=0.55, run_time=0.6) for node in hidden_layer],
            *[Flash(node, color=GREEN, flash_radius=0.65, run_time=0.6) for node in output_layer]
        )
        self.play(*node_flash, run_time=1.2)
        activation_eq = MathTex(r"a = \sigma(Wx + b)").scale(0.9).set_color_by_gradient(BLUE, WHITE)
        activation_eq.next_to(forward_text, DOWN, buff=0.25)
        self.play(Write(activation_eq), run_time=1.0)
        self.wait(1.0)

        self.play(*[line.animate.set_color(GREY) for line in connections], run_time=0.8)
        self.wait(0.6)

        output_callout = Tex("Prediction: Paris", color=GREEN).scale(0.8)
        output_callout.next_to(output_layer, RIGHT, buff=0.8)
        self.play(FadeIn(output_callout, shift=RIGHT * 0.5), run_time=0.8)
        self.wait(1.0)

        loss_text = Tex("Compare to the correct answer", color=RED).scale(0.75)
        loss_text.next_to(forward_text, DOWN, buff=0.35)
        grad_text = Tex("Backpropagation sends gradients backward", color=YELLOW).scale(0.7)
        grad_text.next_to(loss_text, DOWN, buff=0.2)
        self.play(Transform(forward_text, loss_text), run_time=1.0)
        self.play(Write(grad_text), run_time=0.8)

        back_lines = [line.copy().set_color(RED) for line in connections]
        self.play(
            LaggedStart(*[ReplacementTransform(line.copy(), new) for line, new in zip(connections, back_lines)],
                        lag_ratio=0.02, run_time=1.6)
        )
        gradient_formula = MathTex(r"W \leftarrow W - \eta\, \nabla_W L", color=ORANGE).scale(0.85)
        gradient_formula.next_to(grad_text, DOWN, buff=0.25)
        self.play(Write(gradient_formula), run_time=1.0)
        self.wait(1.4)

        self.play(*[line.animate.set_color(GREY) for line in connections], run_time=0.8)
        self.wait(0.6)

        tuning_text = Tex("Weights nudge to improve the response", color=GREEN).scale(0.75)
        tuning_text.next_to(gradient_formula, DOWN, buff=0.3)
        self.play(Write(tuning_text), run_time=1.0)
        pulse_lines = [line.copy().set_color(GREEN) for line in connections[:4]]
        self.play(LaggedStart(*[ReplacementTransform(old, new) for old, new in zip(connections[:4], pulse_lines)],
                               lag_ratio=0.05, run_time=1.2))
        self.play(*[line.animate.set_color(GREY) for line in connections[:4]], run_time=0.8)
        self.wait(1.2)

        step1 = Tex("1) Encode the prompt", color=WHITE).scale(0.8).next_to(neuron_note, DOWN, buff=0.25)
        step2 = Tex("2) Forward pass to outputs", color=WHITE).scale(0.8).next_to(neuron_note, DOWN, buff=0.25)
        step3 = Tex("3) Compare with truth", color=WHITE).scale(0.8).next_to(neuron_note, DOWN, buff=0.25)
        step4 = Tex("4) Send gradients back", color=WHITE).scale(0.8).next_to(neuron_note, DOWN, buff=0.25)
        step5 = Tex("Repeat to learn relationships", color=WHITE).scale(0.8).next_to(neuron_note, DOWN, buff=0.25)

        self.play(ReplacementTransform(forward_text, step1), run_time=0.8)
        self.wait(3)
        self.play(ReplacementTransform(step1, step2), run_time=0.8)
        self.wait(3)
        self.play(ReplacementTransform(step2, step3), run_time=0.8)
        self.wait(3)
        self.play(ReplacementTransform(step3, step4), run_time=0.8)
        self.wait(3)
        self.play(ReplacementTransform(step4, step5), run_time=0.8)
        self.wait(5)

        # Brief look at why activation choices matter
        act_title = Tex("Activation shapes learning", color=WHITE).scale(0.8)
        act_title.next_to(step5, DOWN, buff=0.35)
        relu = FunctionGraph(lambda x: np.maximum(0, x), x_range=[-2, 2], color=BLUE).scale(0.7).shift(RIGHT * 2.2 + DOWN * 0.1)
        tanh_curve = FunctionGraph(lambda x: np.tanh(x), x_range=[-2, 2], color=PURPLE).scale(0.7).shift(LEFT * 2.2 + DOWN * 0.1)
        relu_label = Tex("ReLU", color=BLUE).scale(0.6).next_to(relu, DOWN, buff=0.2)
        tanh_label = Tex("tanh", color=PURPLE).scale(0.6).next_to(tanh_curve, DOWN, buff=0.2)
        act_group = VGroup(act_title, relu, tanh_curve, relu_label, tanh_label)

        self.play(Write(act_title), run_time=0.9)
        self.play(Create(tanh_curve), Write(tanh_label), run_time=1.0)
        self.play(Create(relu), Write(relu_label), run_time=1.0)
        self.wait(1.8)

        tiny_glow = VGroup(*[Circumscribe(node, color=BLUE, time_width=0.8) for node in hidden_layer])
        self.play(*tiny_glow, run_time=1.4)
        self.wait(0.8)

        # Quick glimpse at training progress
        loss_curve = VMobject(color=GREEN)
        loss_curve.set_points_smoothly([
            [-3.0, 1.6, 0],
            [-2.4, 1.0, 0],
            [-1.6, 0.5, 0],
            [-0.8, 0.2, 0],
            [0.4, -0.1, 0],
            [1.6, -0.2, 0],
            [2.4, -0.3, 0],
            [3.0, -0.4, 0],
        ])
        loss_curve.scale(0.35)
        loss_axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 1, 0.2],
            x_length=4,
            y_length=1.5,
            axis_config={"color": GREY, "stroke_width": 2}
        ).scale(0.8)
        loss_axes.move_to(DOWN * 3)
        loss_label = Tex("Loss over training batches", color=WHITE).scale(0.6).next_to(loss_axes, UP, buff=0.15)

        self.play(FadeIn(VGroup(loss_axes, loss_label), shift=DOWN * 0.2), run_time=1.0)
        self.play(Create(loss_curve.move_to(loss_axes.c2p(0, 0.9))), run_time=1.4)
        self.wait(1.2)

        mini_pointer = Dot(color=YELLOW).move_to(loss_curve.get_points()[0])
        tracker = ValueTracker(0)

        def update_pointer(mob):
            idx = int(np.clip(tracker.get_value(), 0, len(loss_curve.get_points()) - 1))
            mob.move_to(loss_curve.get_points()[idx])

        mini_pointer.add_updater(update_pointer)
        self.play(tracker.animate.set_value(len(loss_curve.get_points()) - 1), run_time=2.0)
        mini_pointer.remove_updater(update_pointer)
        self.play(FadeOut(mini_pointer), run_time=0.5)
        self.wait(1.0)

        fade_targets = VGroup(prompt, neuron_note, activation_eq, output_callout, grad_text, gradient_formula, tuning_text, step5, act_group, loss_axes, loss_label, loss_curve)
        self.play(FadeOut(fade_targets, shift=UP * 0.4), run_time=1.2)
        self.wait(2)

        self.play(layers.animate.move_to(ORIGIN), run_time=1.0)
        self.wait(2)

        self.play(FadeOut(VGroup(layers, connections)), run_time=1.2)
        self.wait(1.0)


# manim -pqh video25.py video25
