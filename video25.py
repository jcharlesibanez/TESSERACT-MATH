from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class video25(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Neural Networks in 60 Seconds").set_color_by_gradient(BLUE, WHITE)
        box = SurroundingRectangle(title, color=YELLOW, buff=0.2)
        self.play(Write(title), Create(box), run_time=1)
        box.add_updater(lambda b: b.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        self.wait(0.5)

        subtitle = Tex("Stacks of neurons learn patterns").set_color(TEAL)
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(subtitle, shift=DOWN), run_time=1)
        self.wait(0.5)

        neuron_circle = Circle(radius=0.6, color=BLUE, stroke_width=6)
        neuron_label = Tex("Neuron", color=WHITE).scale(0.8)
        neuron_group = VGroup(neuron_circle, neuron_label)
        neuron_group.next_to(subtitle, DOWN, buff=0.8)
        self.play(Create(neuron_circle), FadeIn(neuron_label), run_time=1)
        self.wait(0.25)

        dendrites = VGroup(
            Line(neuron_circle.get_left()+UP*0.4, neuron_circle.get_center(), stroke_width=5),
            Line(neuron_circle.get_left(), neuron_circle.get_center(), stroke_width=5),
            Line(neuron_circle.get_left()+DOWN*0.4, neuron_circle.get_center(), stroke_width=5),
        )
        axon = Line(neuron_circle.get_center(), neuron_circle.get_right()+RIGHT*0.8, stroke_width=5)
        self.play(Create(dendrites), Create(axon), run_time=0.8)

        neuron_text = Tex(r"Adds weighted inputs\\and applies activation", color=YELLOW).scale(0.7)
        neuron_text.next_to(neuron_group, DOWN, buff=0.6)
        self.play(Write(neuron_text), run_time=0.8)
        self.wait(0.5)

        input_layer = VGroup(
            *[Circle(radius=0.3, color=BLUE).shift(LEFT*3+UP*(i-1)) for i in range(3)]
        )
        hidden_layer = VGroup(
            *[Circle(radius=0.3, color=PURPLE).shift(LEFT*0.6+UP*(i-1)) for i in range(3)]
        )
        output_layer = VGroup(
            *[Circle(radius=0.35, color=GREEN).shift(RIGHT*2+UP*(i-1)) for i in range(2)]
        )

        layers = VGroup(input_layer, hidden_layer, output_layer).arrange(RIGHT, buff=1.3).to_edge(DOWN, buff=1.5)
        input_layer, hidden_layer, output_layer = layers

        connections = VGroup()
        for a in input_layer:
            for b in hidden_layer:
                connections.add(Line(a.get_center(), b.get_center(), stroke_width=3, color=GREY))
        for b in hidden_layer:
            for c in output_layer:
                connections.add(Line(b.get_center(), c.get_center(), stroke_width=3, color=GREY))

        self.play(LaggedStart(
            FadeOut(VGroup(title, subtitle, box, neuron_group, dendrites, axon, neuron_text), shift=UP),
            Create(layers),
            Create(connections),
            lag_ratio=0.15,
            run_time=1.6,
        ))
        self.wait(0.3)

        activations = VGroup(
            *[Dot(point=node.get_center(), color=YELLOW, radius=0.1) for node in input_layer],
            *[Dot(point=node.get_center(), color=ORANGE, radius=0.1) for node in hidden_layer],
            *[Dot(point=node.get_center(), color=GREEN, radius=0.12) for node in output_layer],
        )

        forward_text = Tex("Forward Pass = Multiply + Activate", color=WHITE).scale(0.7)
        forward_text.to_edge(UP, buff=0.8)
        self.play(Write(forward_text), FadeIn(activations), run_time=1)

        waves = VGroup()
        for line in connections:
            wave = Line(line.start, line.end, color=YELLOW, stroke_width=6).set_opacity(0.4)
            waves.add(wave)
        self.play(LaggedStart(*[ReplacementTransform(line.copy(), wave) for line, wave in zip(connections, waves)], lag_ratio=0.02, run_time=1.2))
        self.wait(0.3)

        activation_eq = MathTex(r"a = \sigma(Wx + b)").scale(0.9).set_color_by_gradient(BLUE, WHITE)
        activation_eq.next_to(forward_text, DOWN, buff=0.3)
        self.play(Write(activation_eq), run_time=0.8)
        self.wait(0.4)

        loss_title = Tex("Loss measures error", color=RED).scale(0.8)
        loss_value = MathTex(r"L = \|y_{pred} - y_{true}\|^2", color=RED).scale(0.9)
        loss_group = VGroup(loss_title, loss_value).arrange(DOWN, buff=0.2)
        loss_group.to_edge(UP, buff=1.2)
        self.play(Transform(forward_text, loss_title), Transform(activation_eq, loss_value), run_time=1)
        self.wait(0.4)

        loss_flash = SurroundingRectangle(loss_group, color=RED, buff=0.25, stroke_width=6)
        self.play(Create(loss_flash), run_time=0.6)
        self.wait(0.3)

        gradients_text = Tex("Backpropagation sends gradients backward", color=YELLOW).scale(0.7)
        gradients_text.next_to(loss_group, DOWN, buff=0.4)
        arrows = VGroup()
        for line in connections:
            arrow = Line(line.end, line.start, color=YELLOW, stroke_width=6, buff=0).add_tip(tip_length=0.15)
            arrows.add(arrow)
        self.play(Write(gradients_text), LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.02, run_time=1.2))
        self.wait(0.4)

        gradient_formula = MathTex(r"W \leftarrow W - \eta \nabla_W L", color=ORANGE).scale(0.9)
        gradient_formula.next_to(gradients_text, DOWN, buff=0.3)
        self.play(Write(gradient_formula), run_time=0.7)

        learning_text = Tex("Weights adjust to reduce loss", color=GREEN).scale(0.75)
        learning_text.next_to(gradient_formula, DOWN, buff=0.4)
        self.play(Write(learning_text), run_time=0.7)
        self.wait(0.4)

        highlight_edges = VGroup(*[line.copy().set_color(GREEN) for line in connections[:4]])
        self.play(ReplacementTransform(connections[:4].copy(), highlight_edges), run_time=0.8)
        self.wait(0.3)

        dataset = VGroup(
            Square(side_length=1, color=BLUE).shift(UP*2.5+LEFT*2),
            Triangle(color=YELLOW, fill_opacity=0.2).shift(UP*2.7+LEFT*0.6),
            Circle(radius=0.5, color=GREEN).shift(UP*2.5+RIGHT*1.2),
            RegularPolygon(n=5, color=PURPLE).shift(UP*2.5+RIGHT*3),
        )
        labels = VGroup(
            Tex("Image"), Tex("Sound"), Tex("Text"), Tex("Data")
        )
        for shape, label in zip(dataset, labels):
            label.next_to(shape, DOWN, buff=0.15)
        dataset_group = VGroup(dataset, labels)
        self.play(FadeIn(dataset_group, shift=DOWN), run_time=1)
        self.wait(0.3)

        brace = Brace(dataset_group, DOWN, color=WHITE)
        dataset_caption = brace.get_text("Neural nets learn patterns in many domains")
        dataset_caption.set_color_by_gradient(BLUE, GREEN)
        self.play(Create(brace), Write(dataset_caption), run_time=1)
        self.wait(0.5)

        summary = Tex(r"Neural networks = neurons + activation + backprop + data", color=WHITE).scale(0.7)
        summary.to_edge(DOWN, buff=0.6)
        self.play(Write(summary), run_time=1)
        self.wait(1.5)

        outro = Tex("Thanks for watching!", color=YELLOW)
        outro.scale(0.9).to_edge(DOWN, buff=1.2)
        self.play(FadeOut(VGroup(dataset_group, brace, dataset_caption, loss_flash, gradients_text, gradient_formula, learning_text, arrows, highlight_edges)),
                  FadeOut(layers, connections, activations, forward_text, activation_eq, loss_group, summary),
                  FadeIn(outro, shift=UP),
                  run_time=1.2)
        self.wait(1.5)

# manim -pqh video25.py video25
