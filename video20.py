from manim import *
import numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video20(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("What is the derivative?").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2)
        self.play(Write(title), Create(titleSR), run_time=1)
        
        # Add updater AFTER creation
        titleSR.add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        
        self.play(title.animate.shift(UP*4), Uncreate(titleSR))

        axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 5, 1],
            tips=False,
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        
        function = axes.plot(lambda x: 0.9*x*np.sin(0.8*(x-1.1))+0.9).set_color_by_gradient([BLUE, WHITE])
        self.play(Create(axes), Create(function))

        derivativewritten = Tex("The derivative at a\\\\point is the slope of a\\\\function at that point.").set_color_by_gradient(YELLOW, WHITE
                            ).scale(0.75).move_to(axes.c2p(1.5, 4))
        
        a = ValueTracker(1)

        Pt1 = Dot(
            point=axes.c2p(1, 0.9*a.get_value()*np.sin(0.8*(a.get_value()-1.1))+0.9),
            radius=0.075,
            color=WHITE
        )

        aLn = DashedLine(
            start=axes.c2p(a.get_value(), 0.9*a.get_value()*np.sin(0.8*(a.get_value()-1.1))+0.9),
            end=axes.c2p(a.get_value(), 0)
        )
        aL = MathTex("a").next_to(axes.c2p(1, 0), DOWN).scale(0.8).set_color_by_gradient(BLUE, WHITE)

        fa = DashedLine(
            start=axes.c2p(0, 0.9*a.get_value()*np.sin(0.8*(a.get_value()-1.1))+0.9),
            end=axes.c2p(a.get_value(), 0.9*a.get_value()*np.sin(0.8*(a.get_value()-1.1))+0.9)
        )
        faL = MathTex("f(a)").next_to(axes.c2p(0, 0.9*a.get_value()*np.sin(0.8*(a.get_value()-1.1))+0.9), LEFT).scale(0.8).set_color_by_gradient(BLUE, WHITE)

        directions = Tex("Define two points").scale(0.8).move_to(axes.c2p(1.25, 4))
        d2 = MathTex(r"f'(a)=\lim_{h\to 0} \frac{f(a+h)-f(a)}{x+h-x}").set_color_by_gradient(BLUE, WHITE).scale(0.7).move_to(axes.c2p(1.75, 4.25))
        d3 = MathTex(r"f'(a)=\lim_{h\to 0} \frac{f(a+h)-f(a)}{h}").set_color_by_gradient(BLUE, WHITE).scale(0.7).move_to(axes.c2p(1.75, 4.25))
        fprimea= MathTex("f'(a)").scale(0.8).next_to(directions.get_center(), UP)

        pos2 = ValueTracker(1)

        Pt2 = Dot(
            point=axes.c2p(pos2.get_value(), 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9),
            radius=0.075,
            color=WHITE
        )

        bLn = DashedLine(
            start=axes.c2p(pos2.get_value(), 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9),
            end=axes.c2p(pos2.get_value(), 0)
        )

        fb = DashedLine(
            start=axes.c2p(0, 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9),
            end=axes.c2p(pos2.get_value(), 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9)
        )

        self.play(Write(fprimea))
        self.play(Write(directions), Create(aLn), Write(aL), Create(fa), Create(faL), Create(Pt1), Create(Pt2),
                  Create(bLn), Create(fb))
        
        # Add updaters AFTER objects are animated in
        Pt2.add_updater(lambda d: d.become(Dot(
            point=axes.c2p(pos2.get_value(), 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9),
            radius=0.075,
            color=WHITE
        )))
        
        bLn.add_updater(lambda line: line.become(DashedLine(
            start=axes.c2p(pos2.get_value(), 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9),
            end=axes.c2p(pos2.get_value(), 0)
        )))
        
        fb.add_updater(lambda line: line.become(DashedLine(
            start=axes.c2p(0, 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9),
            end=axes.c2p(pos2.get_value(), 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9)
        )))
        
        self.wait(0.25)
        self.play(pos2.animate.set_value(2.5))

        h = BraceBetweenPoints(
            point_1=axes.c2p(1, 0),
            point_2=axes.c2p(pos2.get_value(), 0),
            direction=UP
        ).set_color_by_gradient([BLUE, WHITE])

        hL = MathTex("h").next_to(h, UP*0.5).scale(0.8).set_color_by_gradient(BLUE, WHITE)
        
        self.play(FadeIn(h, hL), run_time=0.5)
        
        # Add updaters AFTER objects are animated in
        h.add_updater(lambda br: br.become(BraceBetweenPoints(
            point_1=axes.c2p(1, 0),
            point_2=axes.c2p(pos2.get_value(), 0),
            direction=UP
        ).set_color_by_gradient([BLUE, WHITE])))
        
        hL.add_updater(lambda lbl: lbl.become(MathTex("h").next_to(h, UP*0.5).scale(0.8).set_color_by_gradient(BLUE, WHITE)))

        bL = MathTex("a+h").next_to(axes.c2p(pos2.get_value(), 0), DOWN*0.6).scale(0.8).set_color_by_gradient(BLUE, WHITE)
        
        fbL = MathTex("f(a+h)").next_to(axes.c2p(0, 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9), LEFT*0.5).scale(0.8).set_color_by_gradient(BLUE, WHITE)
        
        self.play(FadeIn(bL, fbL), run_time=0.5)
        
        # Add updaters AFTER objects are animated in
        bL.add_updater(lambda lbl: lbl.become(MathTex("a+h").next_to(axes.c2p(pos2.get_value(), 0), DOWN*0.6).scale(0.8).set_color_by_gradient(BLUE, WHITE)))
        
        fbL.add_updater(lambda lbl: lbl.become(MathTex("f(a+h)").next_to(axes.c2p(0, 0.9*pos2.get_value()*np.sin(0.8*(pos2.get_value()-1.1))+0.9), LEFT*0.5).scale(0.8).set_color_by_gradient(BLUE, WHITE)))
        
        self.play(Circumscribe(hL), Circumscribe(faL), Circumscribe(aL), Circumscribe(bL), Circumscribe(fbL), TransformMatchingShapes(fprimea, d2), TransformMatchingShapes(directions, d2))
        self.wait(0.25)
        self.play(TransformMatchingShapes(d2, d3))

        ln = axes.plot(lambda x:
            (0.9 * pos2.get_value() * np.sin(0.8 * (pos2.get_value() - 1.1)) + 0.9 - 
            0.9 * a.get_value() * np.sin(0.8 * (a.get_value() - 1.1)) - 0.9) / 
            (pos2.get_value() - a.get_value()) * 
            (x - a.get_value()) + 
            (0.9 * a.get_value() * np.sin(0.8 * (a.get_value() - 1.1)) + 0.9)
        ).set_color(YELLOW)
        
        self.play(Create(ln))
        
        # Add updater AFTER object is animated in
        ln.add_updater(lambda line: line.become(axes.plot(lambda x:
            (0.9 * pos2.get_value() * np.sin(0.8 * (pos2.get_value() - 1.1)) + 0.9 - 
            0.9 * a.get_value() * np.sin(0.8 * (a.get_value() - 1.1)) - 0.9) / 
            (pos2.get_value() - a.get_value()) * 
            (x - a.get_value()) + 
            (0.9 * a.get_value() * np.sin(0.8 * (a.get_value() - 1.1)) + 0.9)
        ).set_color(YELLOW)))
        
        self.wait(0.5)
        self.play(pos2.animate.set_value(1.000001), FadeOut(bL, fbL, aL, faL, h, hL, aLn, fa, bLn, fb), Pt1.animate.set_color(YELLOW), Pt2.animate.set_color(YELLOW), run_time=2)

        self.wait(2)

        self.play(FadeOut(*[m for m in self.mobjects if m != d3]), d3.animate.move_to(ORIGIN), FadeOut(ln), FadeOut(Pt2))
        self.play(Circumscribe(d3))
        self.wait(2)
        self.play(FadeOut(d3))

# manim -pqh video20.py video20