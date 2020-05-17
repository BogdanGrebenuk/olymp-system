export class NavBarElement {
    constructor(name, link) {
        this.name = name;
        this.link = link;
    }
}

export const HomeElement = new NavBarElement('Home', '/');
export const ContestsElement = new NavBarElement('Contests', '/contests');
export const ContestsNewElement = new NavBarElement('Create contest', '/contests/new');
