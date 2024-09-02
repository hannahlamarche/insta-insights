// This file is auto-generated by @hey-api/openapi-ts

export const $Account = {
    properties: {
        username: {
            type: 'string',
            title: 'Username'
        },
        full_name: {
            type: 'string',
            title: 'Full Name'
        }
    },
    type: 'object',
    required: ['username', 'full_name'],
    title: 'Account',
    example: {
        full_name: 'User Name',
        username: 'user.name'
    }
} as const;

export const $HTTPValidationError = {
    properties: {
        detail: {
            items: {
                '$ref': '#/components/schemas/ValidationError'
            },
            type: 'array',
            title: 'Detail'
        }
    },
    type: 'object',
    title: 'HTTPValidationError'
} as const;

export const $Report = {
    properties: {
        username: {
            type: 'string',
            title: 'Username'
        },
        date: {
            type: 'string',
            format: 'date-time',
            title: 'Date'
        },
        followers: {
            items: {
                '$ref': '#/components/schemas/Account'
            },
            type: 'array',
            title: 'Followers'
        },
        following: {
            items: {
                '$ref': '#/components/schemas/Account'
            },
            type: 'array',
            title: 'Following'
        },
        dont_follow_me_back: {
            items: {
                '$ref': '#/components/schemas/Account'
            },
            type: 'array',
            title: 'Dont Follow Me Back'
        },
        i_dont_follow_back: {
            items: {
                '$ref': '#/components/schemas/Account'
            },
            type: 'array',
            title: 'I Dont Follow Back'
        }
    },
    type: 'object',
    required: ['username', 'date', 'followers', 'following', 'dont_follow_me_back', 'i_dont_follow_back'],
    title: 'Report',
    example: {
        date: '2024-09-01T00:00:00Z',
        dont_follow_me_back: [
            {
                full_name: 'Not Following Back One',
                username: 'dont_follow_me_back1'
            }
        ],
        followers: [
            {
                full_name: 'Follower One',
                username: 'follower1'
            }
        ],
        following: [
            {
                full_name: 'Following One',
                username: 'following1'
            }
        ],
        i_dont_follow_back: [
            {
                full_name: "I Don't Follow Back One",
                username: 'i_dont_follow_back1'
            }
        ],
        username: 'user.name'
    }
} as const;

export const $ValidationError = {
    properties: {
        loc: {
            items: {
                anyOf: [
                    {
                        type: 'string'
                    },
                    {
                        type: 'integer'
                    }
                ]
            },
            type: 'array',
            title: 'Location'
        },
        msg: {
            type: 'string',
            title: 'Message'
        },
        type: {
            type: 'string',
            title: 'Error Type'
        }
    },
    type: 'object',
    required: ['loc', 'msg', 'type'],
    title: 'ValidationError'
} as const;