from manim import *

class video9(MovingCameraScene):
    def construct(self):
        self.play(self.camera.frame.animate.set(width=self.camera.frame.width * 0.65))
        # Title
        title = Text("Related Rates:", font_size=36, color=YELLOW).move_to(ORIGIN)
        subtitle = Text("The Ladder Problem", font_size=28).next_to(title, DOWN, buff=0.2)
        self.play(Write(title), Write(subtitle))
        self.wait(0.15)
        self.play(FadeOut(title), FadeOut(subtitle))

        vpos = 5
        
        # Setup: Wall and ground
        wall = Line(ORIGIN, UP*4, color=GRAY).shift(LEFT*2 + DOWN*2)
        ground = Line(ORIGIN, RIGHT*4, color=GRAY).shift(LEFT*2 + DOWN*2)
        
        self.play(Create(wall), Create(ground))
        
        # Problem statement
        problem = VGroup(
            Text("A 5m ladder slides", font_size=24),
            Text("down a wall", font_size=24)
        ).arrange(DOWN, buff=0.1).to_edge(UP*vpos, buff=0.3)
        self.play(Write(problem), run_time=1)
        
        # Initialize values - start at x=3, y=4
        x_val = ValueTracker(3)
        y_val = ValueTracker(4)
        
        # Create ladder with always_redraw
        ladder = always_redraw(lambda: Line(
            wall.get_start() + UP*y_val.get_value(),
            ground.get_start() + RIGHT*x_val.get_value(),
            color=BLUE,
            stroke_width=8
        ))
        
        self.play(Create(ladder))
        self.wait(0.3)
        
        # Labels
        x_label = always_redraw(lambda: MathTex("x", color=GREEN).next_to(
            ground.get_start() + RIGHT*x_val.get_value()/2, DOWN, buff=0.2
        ))
        y_label = always_redraw(lambda: MathTex("y", color=RED).next_to(
            wall.get_start() + UP*y_val.get_value()/2, LEFT, buff=0.2
        ))
        
        self.play(FadeOut(problem))
        self.play(Write(x_label), Write(y_label))
        
        # Show the constraint equation
        constraint = MathTex("x^2 + y^2 = 25", font_size=32, color=YELLOW).to_edge(UP*vpos, buff=0.3)
        self.play(Write(constraint))
        self.wait(0.5)
        
        # Animate ladder sliding
        question = VGroup(
            Text("Bottom slides at", font_size=22),
            MathTex(r"\frac{dx}{dt} = 2 \text{ m/s}", font_size=28, color=GREEN)
        ).arrange(DOWN, buff=0.15).next_to(constraint, DOWN, buff=0.3)
        
        self.play(Write(question))
        self.wait(0.3)
        
        # Animate the sliding - both x and y move together
        # x goes from 3 to 4.5, y goes from 4 to sqrt(25-20.25)≈2.18
        dist = 4
        self.play(
            x_val.animate.set_value(dist),
            y_val.animate.set_value(np.sqrt(25 - dist**2)),
            run_time=2,
            rate_func=linear
        )
        self.wait(0.3)
        
        # Differentiate
        self.play(FadeOut(constraint))
        diff_eq = MathTex(
            r"2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0",
            font_size=28
        ).to_edge(UP*vpos, buff=0.3)
        self.play(Write(diff_eq))
        self.wait(0.5)
        
        # Solve for dy/dt
        solve = MathTex(
            r"\frac{dy}{dt} = -\frac{x}{y}\frac{dx}{dt}",
            font_size=28,
            color=RED
        ).move_to(diff_eq.get_center())
        self.play(ReplacementTransform(diff_eq, solve), FadeOut(question))
        self.wait(0.5)
        
        # Plug in values
        values = VGroup(
            MathTex(r"\text{When } x = 4 \text{ m}, y = 3\text{ m}:", font_size=22),
            MathTex(r"\frac{dy}{dt} = -\frac{4}{3}(2)", font_size=26),
        ).arrange(DOWN, buff=0.2).next_to(solve, DOWN, buff=0.3)
        self.play(Write(values))
        self.wait(0.5)
        
        # Final answer
        answer = MathTex(
            r"\frac{dy}{dt} = -\frac{8}{3} \text{ m/s}",
            font_size=32,
            color=YELLOW
        )
        answer_box = SurroundingRectangle(answer, color=YELLOW, buff=0.15)
        answer_group = VGroup(answer, answer_box).move_to(values.get_center())
        
        self.play(ReplacementTransform(values, answer))
        self.wait(0.1)
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != answer])
        self.wait(0.5)
        self.play(answer.animate.move_to(ORIGIN))
        answer = answer.move_to(ORIGIN)
        a_box = SurroundingRectangle(answer, color=YELLOW, buff=0.15)
        self.play(Create(a_box))
        self.play(FadeOut(answer), FadeOut(a_box))


# manim -pqh video9.py video9