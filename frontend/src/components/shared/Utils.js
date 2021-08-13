// utility class to make passing classnames to components easier

export function classNames(...classes) {
    return classes.filter(Boolean).join(" ");
}