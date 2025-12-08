from manim import *
import numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video19(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Basic Geometry Formulas").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2).add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        self.play(Write(title), Create(titleSR), run_time=1)
        self.play(title.animate.shift(UP*4), Uncreate(titleSR))

        square = Square().set_color_by_gradient([BLUE, WHITE])
        squareLabel = Tex("Square").set_color_by_gradient(BLUE, WHITE).shift(UP*2.5)
        squareSideLabel1 = MathTex("s").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(square, LEFT)
        squareSideLabel2 = MathTex("s").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(square, DOWN)
        sqArea = MathTex("Area = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        sqAream = MathTex("Area = s\cdot s").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        sqAreaf = MathTex("A = s^2").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        squareSideLabel3 = MathTex("s").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(square, UP)
        squareSideLabel4 = MathTex("s").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(square, RIGHT)
        sqPerimeter = MathTex("Perimeter = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        sqPerimeterm = MathTex("Perimeter = s+s+s+s").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        sqPerimeterf = MathTex("P = 4s").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)

        self.play(Create(square), Write(squareLabel))
        self.play(Write(sqArea), Write(squareSideLabel1), Write(squareSideLabel2))
        self.play(square.animate.set_opacity(0.5))
        self.play(Indicate(squareSideLabel1), Indicate(squareSideLabel2), TransformMatchingShapes(sqArea, sqAream))
        self.wait(0.25)
        self.play(TransformMatchingShapes(sqAream, sqAreaf))
        self.play(Circumscribe(sqAreaf))
        self.play(square.animate.set_style(fill_color=None, fill_opacity=0, stroke_width=8, stroke_color=YELLOW), Write(squareSideLabel3), Write(squareSideLabel4), 
                  Write(sqPerimeter))
        self.play(Indicate(squareSideLabel1), Indicate(squareSideLabel2), Indicate(squareSideLabel3), Indicate(squareSideLabel4),
                  TransformMatchingShapes(sqPerimeter, sqPerimeterm))
        self.wait(0.25)
        self.play(TransformMatchingShapes(sqPerimeterm, sqPerimeterf))
        self.play(Circumscribe(sqPerimeterf))

        self.wait(1)

        rectangle = Rectangle().set_color_by_gradient([BLUE, WHITE])
        rectLabel = Tex("Rectangle").set_color_by_gradient(BLUE, WHITE).shift(UP*2.5)
        rectSideLabel1 = MathTex("w").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(rectangle, LEFT)
        rectSideLabel2 = MathTex("l").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(rectangle, DOWN)
        rectArea = MathTex("Area = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        rectAream = MathTex("Area = w\cdot l").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        rectAreaf = MathTex("A = w l").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        rectSideLabel3 = MathTex("l").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(rectangle, UP)
        rectSideLabel4 = MathTex("w").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(rectangle, RIGHT)
        rectPerimeter = MathTex("Perimeter = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        rectPerimeterm = MathTex("Perimeter = w+l+w+l").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        rectPerimeterm2 = MathTex("Perimeter = 2w+2l").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        rectPerimeterf = MathTex("P = 2(w+l)").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)

        self.play(TransformMatchingShapes(square, rectangle), TransformMatchingShapes(squareLabel, rectLabel),
                  FadeOut(sqAreaf, sqPerimeterf, squareSideLabel1, squareSideLabel2, squareSideLabel3, squareSideLabel4))

        self.play(Write(rectArea), Write(rectSideLabel1), Write(rectSideLabel2))
        self.play(rectangle.animate.set_opacity(0.5))
        self.play(Indicate(rectSideLabel1), Indicate(rectSideLabel2), TransformMatchingShapes(rectArea, rectAream))
        self.wait(0.25)
        self.play(TransformMatchingShapes(rectAream, rectAreaf))
        self.play(Circumscribe(rectAreaf))
        self.play(rectangle.animate.set_style(fill_color=None, fill_opacity=0, stroke_width=8, stroke_color=YELLOW), Write(rectSideLabel3), Write(rectSideLabel4), 
                  Write(rectPerimeter))
        self.play(Indicate(rectSideLabel1), Indicate(rectSideLabel2), Indicate(rectSideLabel3), Indicate(rectSideLabel4),
                  TransformMatchingShapes(rectPerimeter, rectPerimeterm))
        self.play(TransformMatchingShapes(rectPerimeterm, rectPerimeterm2))
        self.wait(0.25)
        self.play(TransformMatchingShapes(rectPerimeterm2, rectPerimeterf))
        self.play(Circumscribe(rectPerimeterf))

        self.wait(1)

        circle = Circle().set_color_by_gradient([BLUE, WHITE])
        circleLabel = Tex("Circle").set_color_by_gradient(BLUE, WHITE).shift(UP*2.5)
        radiusLine = Line(start=ORIGIN, end=RIGHT).set_color_by_gradient(BLUE, WHITE)
        radiusLabel = MathTex("r").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(radiusLine, UP*0.5)
        circArea = MathTex("Area = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        circAream = MathTex("Area = \pi \cdot r \cdot r").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        circAreaf = MathTex("A = \pi r^2").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2)
        circCircumference = MathTex("Circumference = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        circCircumferencem = MathTex("Circumference = 2\cdot \pi \cdot r").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)
        circCircumferencef = MathTex("C = 2\pi r").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3)

        self.play(TransformMatchingShapes(rectangle, circle), TransformMatchingShapes(rectLabel, circleLabel),
                  FadeOut(rectAreaf, rectPerimeterf, rectSideLabel1, rectSideLabel2, rectSideLabel3, rectSideLabel4))

        self.play(Write(circArea), Write(radiusLabel), Create(radiusLine))
        self.play(circle.animate.set_opacity(0.5))
        self.play(Indicate(radiusLabel), TransformMatchingShapes(circArea, circAream))
        self.wait(0.25)
        self.play(TransformMatchingShapes(circAream, circAreaf))
        self.play(Circumscribe(circAreaf))
        self.play(circle.animate.set_style(fill_color=None, fill_opacity=0, stroke_width=8, stroke_color=YELLOW), Write(circCircumference))
        self.play(Indicate(radiusLabel), TransformMatchingShapes(circCircumference, circCircumferencem))
        self.wait(0.25)
        self.play(TransformMatchingShapes(circCircumferencem, circCircumferencef))
        self.play(Circumscribe(circCircumferencef))

        self.wait(1)

        triArSquare = Square().set_fill(YELLOW, opacity=0.15).set_stroke(opacity=0)
        bl = triArSquare.get_critical_point(LEFT + DOWN)
        br = triArSquare.get_critical_point(RIGHT + DOWN)
        tl = triArSquare.get_critical_point(LEFT + UP)
        triArSquaref = Polygon(bl, br, tl, color=YELLOW).set_opacity(0.15)
        triangle = Polygon(bl, br, tl).set_color_by_gradient([BLUE, WHITE])
        triangleLabel = Tex("Triangle").set_color_by_gradient(BLUE, WHITE).shift(UP*2.5)
        vertices = triangle.get_vertices()
        top_point = max(vertices, key=lambda p: p[1])
        base_y = min(p[1] for p in vertices)
        foot = np.array([top_point[0], base_y, 0])
        heightLine = Line(foot, top_point).set_color_by_gradient([BLUE, WHITE])
        heightLabel = MathTex("h").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(heightLine, LEFT*1.55, buff=0.1)
        baseLabel = MathTex("b").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(triangle, DOWN*0.5, buff=0.5)
        aLabel = MathTex("a").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(heightLine, LEFT*1.5, buff=0.1)
        cLabel = MathTex("c").set_color_by_gradient(BLUE, WHITE).scale(0.75).move_to(triArSquare.get_center()+UR*0.15)
        triArea = MathTex("Area = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2.5)
        triAream = MathTex("Area = b\cdot h").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2.5)
        triAreaf = MathTex("A = \\frac{b h}{2}").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2.5)
        triPyth = MathTex("a^2 + b^2 = c^2").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*3.5)

        self.play(TransformMatchingShapes(circle, triangle), TransformMatchingShapes(circleLabel, triangleLabel),
                  FadeOut(circAreaf, circCircumferencef, radiusLabel, radiusLine))

        self.play(Write(triArea), Write(baseLabel), Write(heightLabel), Create(heightLine))
        self.play(triangle.animate.set_opacity(0.5))
        self.play(Indicate(heightLabel), Indicate(baseLabel), TransformMatchingShapes(triArea, triAream), FadeIn(triArSquare))
        self.wait(0.25)
        self.play(TransformMatchingShapes(triAream, triAreaf), TransformMatchingShapes(triArSquare, triArSquaref), Circumscribe(triAreaf))
        self.wait(0.25)
        self.play(TransformMatchingShapes(heightLabel, aLabel), Write(cLabel))
        self.play(Indicate(aLabel), Indicate(baseLabel), Indicate(cLabel), Write(triPyth), FadeOut(triArSquaref))
        self.play(Circumscribe(triPyth))
        self.wait(1)

        trapezoid = Polygon(
            [-2, -1, 0], [2, -1, 0],
            [1.5, 1, 0], [-1.5, 1, 0]
        ).set_color_by_gradient([BLUE, WHITE])
        trapLabel = Tex("Trapezoid").set_color_by_gradient(BLUE, WHITE).shift(UP*2.5)
        trapSideLabel1 = MathTex("a").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(rectangle, UP)
        trapSideLabel2 = MathTex("b").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(rectangle, DOWN)
        trapArea = MathTex("Area = ").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2.5)
        trapAream = MathTex("Area = \\frac{h(a+b)}{2}").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2.5)
        trapAreaf = MathTex("A = \\frac{a+b}{2}h").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(DOWN*2.5)
        trapHeightLine = DashedLine(start=[-1.5, 1, 0], end=[-1.5, -1, 0])
        trapHeightLabel = MathTex("h").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(trapHeightLine, RIGHT)

        self.play(TransformMatchingShapes(triangle, trapezoid), TransformMatchingShapes(triangleLabel, trapLabel),
                  FadeOut(triAreaf, heightLabel, baseLabel, aLabel, cLabel, heightLine, triPyth))

        self.play(Write(trapArea), Write(trapSideLabel1), Write(trapSideLabel2), Create(trapHeightLine), Write(trapHeightLabel))
        self.play(trapezoid.animate.set_opacity(0.5))
        self.play(Indicate(trapSideLabel1), Indicate(trapSideLabel2), TransformMatchingShapes(trapArea, trapAream))
        self.wait(0.25)
        self.play(TransformMatchingShapes(trapAream, trapAreaf))
        self.play(Circumscribe(trapAreaf))

        self.wait(1)
        self.play(FadeOut(*[m for m in self.mobjects if m is not trapAreaf]))
        sqAreaf.move_to(ORIGIN).shift(UP*4)
        sqPerimeterf.move_to(ORIGIN).shift(UP*3)
        rectAreaf.move_to(ORIGIN).shift(UP*2)
        rectPerimeterf.move_to(ORIGIN).shift(UP*1)
        circAreaf.move_to(ORIGIN)
        circCircumferencef.move_to(ORIGIN).shift(DOWN*1)
        triAreaf.move_to(ORIGIN).shift(DOWN*2)
        triPyth.move_to(ORIGIN).shift(DOWN*3)
        self.play(trapAreaf.animate.shift(DOWN*1.5))
        self.play(Write(sqAreaf), Write(sqPerimeterf), Write(rectAreaf), Write(rectPerimeterf), Write(circAreaf), Write(circCircumferencef),
                  Write(triAreaf), Write(triPyth))
        formulas = VGroup(sqAreaf, sqPerimeterf, rectAreaf, rectPerimeterf, circAreaf, circCircumferencef, triAreaf, triPyth, trapAreaf)
        self.play(Circumscribe(formulas))
        self.wait(2)
        self.play(FadeOut(*[m for m in self.mobjects]))

# manim -pqh video19.py video19