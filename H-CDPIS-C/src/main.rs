use fltk::{prelude::*, *, app::screen_size, draw::draw_box, enums::FrameType};

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
    let height = screen_size.1 as i32;
    let mut arrival_time = frame::Frame::new(0, 0, width / 4, height / 4, "11:39");
    arrival_time.set_label_color(enums::Color::from_hex(0xffffff));
    arrival_time.set_label_size(height / 8);
    
    let mut train_number = frame::Frame::new(0, height / 4, width / 4, height / 4, "R 76901");
    train_number.set_label_color(enums::Color::from_hex(0xffffff));
    train_number.set_label_size(arrival_time.label_size() / 3);
    train_number.set_align(enums::Align::Top);

    let mut train_destination = frame::Frame::new(width / 4, 0, (width / 4) * 3, height / 4, "Warszawa Główna");
    train_destination.set_label_size(height / 8);
    train_destination.set_label_color(enums::Color::from_hex(0xffffff));

    // let background = draw_box(enums::FrameType::FlatBox, width / 4, 0, (width / 4) * 3, height / 4, enums::Color::from_hex(0x000000));
    let mut train_name = frame::Frame::new(width / 4, height - (height / 10), (width / 4) * 3, height / 7, "*** Choroszczanin ***");
    train_name.set_color(enums::Color::White);
    train_name.set_frame(FrameType::FlatBox);


    win.end();
    win.show();

    app.run().unwrap();
}