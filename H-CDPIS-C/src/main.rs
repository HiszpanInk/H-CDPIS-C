use fltk::{prelude::*, *, app::screen_size};

fn main() {
    let (r, g, b) = utils::hex2rgb(0x0804fc);

    let app = app::App::default();

    // global theming
    app::background(r, g, b); // background color. For input/output and text widgets, use app::background2
    app::foreground(20, 20, 20); // labels
    app::set_font(enums::Font::Courier);
    app::set_font_size(16);
    app::set_frame_type(enums::FrameType::RFlatBox);
    app::set_visible_focus(false);

    // regular widget code
    let mut win = window::Window::default();
    win.fullscreen(true);

    let screen_size = screen_size();
    let width = screen_size.0 as i32;
    // let height = screen_size.1 as i32;
    let mut frame = frame::Frame::new(width / 2, 0, 100, 50, "Defaults");
    frame.set_label_color(enums::Color::from_hex(0xffffff));


    win.end();
    win.show();

    app.run().unwrap();
}